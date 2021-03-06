# Copyright (c) 2016, MD2K Center of Excellence
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from cerebralcortex.kernel.datatypes.annotationstream import AnnotationStream
from cerebralcortex.kernel.datatypes.datastream import DataStream


def ECGDataQuality(datastream: DataStream,
                   windowsize: float = 5.0,
                   bufferLength: int = 3,
                   acceptableOutlierPercent: int = 50,
                   outlierThresholdHigh: int = 4500,
                   outlierThresholdLow: int = 20,
                   badSegmentThreshod: int = 2,
                   ecgBandLooseThreshold: int = 47) -> AnnotationStream:
    """

    :param datastream:
    :param windowsize:
    :param bufferLength:
    :param acceptableOutlierPercent:
    :param outlierThresholdHigh:
    :param outlierThresholdLow:
    :param badSegmentThreshod:
    :param ecgBandLooseThreshold:
    :return:
    """
    # windows = window(datastream.datapoints, window_size=windowsize)

    # TODO: Do something with windows here

    result = DataStream.from_datastream(input_streams=[datastream])

    # Do something here for data quality
    # ecgQuality = []
    # for i in range(1, 10):
    #     ecgQuality.append(Span(result.getID(),
    #                            starttime=datetime.now(),
    #                            endtime=datetime.now(),
    #                            label=DataQuality.GOOD))
    #
    # result.set_spans(ecgQuality)

    return result


def RIPDataQuality(datastream: DataStream,
                   windowsize: float = 5.0,
                   bufferLength=5,
                   acceptableOutlierPercent=50,
                   outlierThresholdHigh=4500,
                   outlierThresholdLow=20,
                   badSegmentThreshod=2,
                   ripBandOffThreshold=20,
                   ripBandLooseThreshold=150) -> AnnotationStream:
    """

    :param datastream:
    :param windowsize:
    :param bufferLength:
    :param acceptableOutlierPercent:
    :param outlierThresholdHigh:
    :param outlierThresholdLow:
    :param badSegmentThreshod:
    :param ripBandOffThreshold:
    :param ripBandLooseThreshold:
    :return:
    """
    # windows = window(datastream.datapoints, window_size=windowsize)

    # TODO: Do something with windows here

    result = DataStream.from_datastream(input_streams=[datastream])

    # # Do something here for data quality
    # ripQuality = []
    # for i in range(1, 10):
    #     ripQuality.append(Span(result.getID(),
    #                            starttime=datetime.now(),
    #                            endtime=datetime.now(),
    #                            label=DataQuality.GOOD))
    #
    # result.set_spans(ripQuality)

    return result
