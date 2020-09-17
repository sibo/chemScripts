#!/bin/bash
cat > calcTrj.nw << EOM
memory heap 200 mb stack 1000 mb global 2800 mb
start calc
title "B3LYP-D3/def2-SVP/LOOSE"
echo
charge 0
dft
    grid medium
    mult 1
    xc b3lyp
    disp vdw 3
    iterations 200
    convergence energy 1d-6
    print low
    direct
end
basis smaller spherical
  * library def2-sv(p)
end
basis small spherical
  * library def2-svp
end
basis large spherical
  * library def2-tzvp
end
basis "cd basis" spherical
  * library "Weigend Coulomb Fitting"
end
driver
  gmax 0.002 ; grms 0.0003 ; xrms 1 ; xmax 1
  maxiter 400
end
#task shell "mkdir -p opt"

EOM
#numConfs=$(grep "unique conformers" ../crest.out | awk '{print $NF}')
numConfs=0
readConfs=False
while read first second rest
do
	#echo "1 = $first 2 = $second rest = $rest"
	if [[ $first = "number" ]] && [[ $second = "of" ]]
	then
		readConfs=True
	elif [ $readConfs = True ]
	then
		if [ $second \< 2 ]
		then
			((numConfs++))
		else
			readConfs=False
		fi
	fi
done < "../crest.out"

echo "$numConfs conformers with deltaE < 2.0 kcal/mol"

for i in $(seq 1 $numConfs)
do
  cat >> calcTrj.nw << EOM
### conf $i
geometry units angstroms
  load frame $i ../crest_conformers.xyz
end
#driver
#  xyz opt/opt$i
#end
set "ao basis" smaller
dft
  vectors input atomic output smaller.mos
end
task dft optimize
#set "ao basis" small
#dft
#  vectors input project smaller smaller.mos output small.mos
#end
#task dft optimize
task shell "echo conf $i complete"

EOM
done
