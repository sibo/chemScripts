#!/bin/bash
cat > calcTrj.nw << EOM
memory heap 200 mb stack 1000 mb global 2800 mb
start calc
title "B97-D3/def2-TZVP//B97-D3/def2-SVP"
echo
charge 0
dft
    grid fine
    mult 1
    xc becke97-d
    disp vdw 3
    iterations 100
    convergence energy 1d-10
    print low
    direct
end
basis small
  * library def2-svp
end
basis large 
  * library def2-tzvp
end
driver
  maxiter 400
end

EOM
for i in {1..10}
do
  cat >> calcTrj.nw << EOM
### conf $i
geometry units angstroms
  load frame $i crest_conformers.xyz
end
task shell "mkdir -p opt$i"
driver
  xyz opt$i/
end
set "ao basis" small
dft
  vectors input atomic output small.mos
end
task dft optimize
set "ao basis" large
dft
  vectors input project small small.mos output large.mos
end
task dft energy
task shell "echo conf $i complete"

EOM
done
