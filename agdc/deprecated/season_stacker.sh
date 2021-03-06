#!/bin/bash

#===============================================================================
# Copyright 2015 Geoscience Australia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

#PBS -P v10
#PBS -q normal
#PBS -l walltime=08:00:00,mem=12GB,ncpus=1
#PBS -l wd
#@#PBS -m e
##PBS -M alex.ip@ga.gov.au

umask 0007

MODULEPATH=/projects/u46/opt/modules/modulefiles:$MODULEPATH

module load python/2.7.5
module load datacube
module load gdal
module load pyephem
module load numexpr
module load ga-neo-landsat-processor
module load psycopg2

#python /home/547/axi547/datacube/index_stacker.py -x 144 -y -36 -o /short/v10/mdb_indices $@
#export DATACUBE_ROOT=$(readlink -f ${0%/*})

export DATACUBE_ROOT=/projects/u46/opt/modules/datacube/0.1.0

python ${DATACUBE_ROOT}/season_stacker.py $@
