#! /usr/bin/env python
import sys
sys.path.insert(0,'/home/aryaf/Pipelines/A2Hack/A2HHDataCortex/source')


flux_mode = False
if flux_mode :
   import matplotlib
   matplotlib.use('Agg')


input = int( sys.argv[1] )

if input == 0 :
   from learning import learningPipeline
   learningPipeline()
if input == 1 :
   pass

