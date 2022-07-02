del %1.pot
pybabel extract --mapping babel.cfg --add-comments="PREVOD:" --output %1.pot ./
pybabel update --input-file %1.pot --output-dir translations/ --domain %1
