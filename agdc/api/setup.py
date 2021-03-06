#!/usr/bin/env python

# ===============================================================================
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
# ===============================================================================


__author__ = "Simon Oldfield"


from setuptools import setup


setup(name="agdc-api",
      version="0.1.0-b20150513",
      package_dir={"": "source/main/python", "test": "source/test/python"},
      packages=["datacube", "datacube.api", "datacube.api.tool", "datacube.api.workflow"],
      scripts=[
          # Tools
          "source/main/python/datacube/api/tool/retrieve_pixel_time_series.py",
          "source/main/python/datacube/api/tool/retrieve_dataset.py",
          "source/main/python/datacube/api/tool/retrieve_dataset_stack.py",
          "source/main/python/datacube/api/tool/retrieve_aoi_time_series.py",

          # Workflows
          "source/main/python/datacube/api/workflow/band_stack.py"],
      author="Geoscience Australia",
      maintainer="Geoscience Australia",
      description="AGDC API",
      license="BSD 3",
      requires=["gdal", "numpy", "scipy", "psycopg2", "enum34", "psutil"]
)
