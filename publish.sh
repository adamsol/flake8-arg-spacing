
pip install --upgrade build twine
rm dist/*
python -m build

read -p "Package built, press Enter to upload to PyPI"
twine upload dist/*
