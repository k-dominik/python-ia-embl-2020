cd ./notebooks # nbconvert needs to run in the same dir

# relative figure paths do not work
# with --to pdf
# https://github.com/jupyter/nbconvert/issues/136
# convert to tex first, then run pdflatex

for f in *ipynb;
do
    echo -e "\nProcessing $f file..\n";
    jupyter nbconvert --to latex $f
    echo "$?"
done

# run pdflatex
for f in *tex;
do
    echo -e "\npdflatex $f file..\n";
    pdflatex -interaction=nonstopmode $f
    echo "$?"
done

mv *pdf ../pdfs

# clean up
rm *log
rm *out
rm *aux
rm *tex

cd -
