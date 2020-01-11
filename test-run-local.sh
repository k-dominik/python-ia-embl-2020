set -xe
python clean-ipnb.py ./notebooks stripview
set +e
pytest -v --nb-test-files --nb-exec-timeout=30
set -e
python clean-ipnb.py ./notebooks restore
