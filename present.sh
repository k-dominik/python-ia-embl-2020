set -x
echo "before"
cp -rv ./fig notebooks/
python clean-ipnb.py $1 prepare4slides
jupyter nbconvert $1 --to slides --reveal-prefix ../reveal.js --post serve
echo "after"
python clean-ipnb.py $1 restore
rm -rfv ./notebooks/fig
