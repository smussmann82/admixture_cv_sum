# admixture_cv_sum
Summarizes the output of cross-validation values for multiple runs of admixture

##Usage:

This tutorial assumes you have already processed your data according to the instructions in the distruct-rerun repository (https://github.com/smussmann82/distruct-rerun).

Change directories into the directory where you saved your cv_file.txt file.  Execute the following code (assuming admixture_cv_sum.py is installed somewhere in your path):
```
admixture_cv_sum.py -c cv_file.txt
```
The default file name accepted by admixture_cv_sum is actually cv_file.txt, so the same could have been accomplished by simply typing "admixture_cv_sum.py" in this case.  However, if you changed the name of cv_file.txt then you must use the -c flag to specify the input.

The output of this program is a plot of boxplots representing the variation in the CV values found by different runs of ADMIXTURE.  The X axis of the plot corresponds to K values, while the Y axis corresponds to the CV values.  Lower CV values are preferred.  The output file will be named "cv_file.png" unless you use the -o option to specify a custom file name.  

**Assuming you followed the instructions from the distruct-rerun repository, you can now cd back to your CLUMPAK output.**  The distruct-rerun repository created a folder within your CLUMPAK results directory named "best_results" which contains the data necessary to rerun distruct on any K value within the range you specified when you ran that code.  For example, if you found K=4 to be the best value, you can now rerun distruct on that file with a command such as the following:
```
distruct -d drawparams.4
```
