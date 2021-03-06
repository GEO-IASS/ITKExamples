#!/usr/bin/env python

#=========================================================================
#
#  Copyright Insight Software Consortium
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#=========================================================================

import sys

import itk

if len(sys.argv) != 4:
    print("Usage: " + sys.argv[0] + "<InputFileName> "
          "<InputFileName> <OutputFileName> <K: ExpNegative parameter>")
    sys.exit(1)

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
k = float(sys.argv[3])

Dimension = 2

InputPixelType = itk.UC
InputImageType = itk.Image[InputPixelType, Dimension]

ReaderType = itk.ImageFileReader[InputImageType]
reader = ReaderType.New()
reader.SetFileName(inputFileName)

OutputPixelType = itk.D
OutputImageType = itk.Image[OutputPixelType, Dimension]

FilterType = itk.ExpNegativeImageFilter[InputImageType, OutputImageType]
expFilter = FilterType.New()
expFilter.SetInput(reader.GetOutput())
expFilter.SetFactor(k)

WriterType = itk.ImageFileWriter[OutputImageType]
writer = WriterType.New()
writer.SetFileName(outputFileName)
writer.SetInput(expFilter.GetOutput())

writer.Update()
