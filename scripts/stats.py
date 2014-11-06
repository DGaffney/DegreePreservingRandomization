#!/usr/bin/python
#only works with python 2.6+
#usage python scripts/stats.py [infile_name] [outfile_name]
import sys
import igraph
import csv
g = igraph.Graph.Read_Ncol(sys.argv[1])
filename = "stats_{0}.csv".format(sys.argv[1])
vertices = []
for v in g.vs:
  vertices.append(v['name'])

with open(filename, 'w') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  writer.writerow(["vertices", vertices])
  writer.writerow(["diameter", g.diameter(directed=True, unconn=True)])
  writer.writerow(["reciprocity", g.reciprocity()])
  writer.writerow(["betweenness", g.betweenness(vertices=None, directed=True, cutoff=None)])
  writer.writerow(["average_path_length", g.average_path_length(directed=True, unconn=True)])
  # writer.writerow(["modularity", g.community_optimal_modularity()])
  # writer.writerow(["clusters", g.clusters(mode=STRONG)])
  writer.writerow(["cocitation", g.cocitation(vertices=None)])
