# Copyright 2019,2020 NXP
#
# SPDX-License-Identifier: Apache-2.0
#

ADD_SUBDIRECTORY(unity)

IF(SSS_HAVE_HOSTCRYPTO_OPENSSL)
    IF(WithCodeCoverage AND SSS_HAVE_HOST_PCWINDOWS)
    ELSE()
        INCLUDE(paho.cmake)
    ENDIF()
    IF(NOT SSS_HAVE_HOST_LINUX_LIKE)
        ADD_SUBDIRECTORY(openssl)
    ENDIF()
ENDIF()
