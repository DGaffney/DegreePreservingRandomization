# usage: Rscript rewirer.r --file ~/536bfe530765e0da87000296_536bfe540765e0da870002a9_1_1400096463.csv --iterations 10000 --outfile 536bfe530765e0da87000296_536bfe540765e0da870002a9_1_1400096463_rewired.csv
library(igraph)
library(car)
library(getopt)
spec <- matrix(c(
        'file', 'f', 1, "character", "Filename",
        'iterations', 'i', 1, "character", "Number of iterations for network rewiring",
        'outfile', 'o', 1, "character", "Outfile to write to"
),ncol=5,byrow=T)

opt = getopt(spec);
g=graph.data.frame(read.csv(opt$file, T), T)
g2 <- rewire(g,niter=opt$iterations)
print(g2)
write.table(get.edgelist(g2), opt$outfile)