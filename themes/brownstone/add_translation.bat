pybabel extract --mapping babel.cfg --output %1.pot ./
pybabel init --locale %2 --input-file %1.pot --output-dir translations --domain %1
