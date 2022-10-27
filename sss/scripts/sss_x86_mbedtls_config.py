#
# Copyright 2018 NXP
# SPDX-License-Identifier: Apache-2.0
#
#

import os
from sss_mbedtls_config_common import *

HEADER_FILE = os.path.abspath(os.path.dirname(__file__)) + os.sep + ".." + os.sep + "port" + os.sep + "default" + os.sep + "sss_x86_mbedtls_config.h"

# [Macro to define, dependencies...]
DEFINE_MACROS = [
    ["MBEDTLS_CMAC_C",
        # Doc 
        None
    ],
    # L1
    ["MBEDTLS_ECP_ALT", 
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        # Doc 
        "/*\n\
 * When replacing the elliptic curve module, pleace consider, that it is\n\
 * implemented with two .c files:\n\
 *      - ecp.c\n\
 *      - ecp_curves.c\n\
 * You can replace them very much like all the other MBEDTLS__MODULE_NAME__ALT\n\
 * macros as described above. The only difference is that you have to make sure\n\
 * that you provide functionality for both .c files.\n\
 */"
    ],
    ["MBEDTLS_ECDH_ALT", 
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        # Doc 
        # Adding doc for ECDSA_VERIFY_ALT here
        "/**\n\
 * - MBEDTLS_ECDSA_VERIFY_ALT\n\
 * To use SE for all public key ecdsa verify operation, enable MBEDTLS_ECDSA_VERIFY_ALT\n\
 */\n\
// #ifndef MBEDTLS_ECDSA_VERIFY_ALT\n\
//     #define MBEDTLS_ECDSA_VERIFY_ALT\n\
// #endif // MBEDTLS_ECDSA_VERIFY_ALT\n"
    ],
    ["MBEDTLS_ECDH_GEN_PUBLIC_ALT", 
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        # Doc 
        None
    ],
    ["MBEDTLS_ECDH_COMPUTE_SHARED_ALT", 
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        # Doc 
        None
    ],
    # To use SE for all public key ecdsa verify operation, enable MBEDTLS_ECDSA_VERIFY_ALT
    # ["MBEDTLS_ECDSA_VERIFY_ALT",
    #     # dependencies
    #     " SSS_HAVE_MBEDTLS_ALT",
    # ]
    # L2
    ["MBEDTLS_RSA_ALT", 
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_RSA",
        # Doc 
        None
    ],
]

# [Macro to undefine, dependencies...]
UNDEFINE_MACROS = [
    ["MBEDTLS_SELF_TEST",
        # Doc 
        None
    ],
    ["MBEDTLS_PSA_CRYPTO_C",
        # Doc 
        None
    ],
    ["MBEDTLS_PSA_CRYPTO_STORAGE_C",
        # Doc 
        None
    ],
    ["MBEDTLS_PSA_ITS_FILE_C",
        # Doc 
        None
    ],
    # L1
    # L2
    ["MBEDTLS_ECP_DP_SECP192R1_ENABLED", 
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_ECP_DP_SECP224R1_ENABLED",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_ECP_DP_SECP384R1_ENABLED",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_ECP_DP_SECP521R1_ENABLED",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_ECP_DP_SECP192K1_ENABLED",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_ECP_DP_SECP224K1_ENABLED",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_ECP_DP_SECP256K1_ENABLED",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_ECP_DP_BP256R1_ENABLED",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_ECP_DP_BP384R1_ENABLED",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_ECP_DP_BP512R1_ENABLED",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_ECP_DP_CURVE25519_ENABLED",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_ECP_DP_CURVE448_ENABLED",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
    ["MBEDTLS_SHA512_C",
        # dependencies
        " SSS_HAVE_MBEDTLS_ALT",
        " SSS_HAVE_MBEDTLS_ALT_A71CH",
        # Doc 
        None
    ],
]

PLATFORM_MEMORY_DEFINE = [
    ["MBEDTLS_PLATFORM_MEMORY",
        # Doc 
        None
    ],
]
PLATFORM_MEMORY_UNDEFINE = [
    ["MBEDTLS_PLATFORM_STD_CALLOC",
        # Doc 
        None
    ],
    ["MBEDTLS_PLATFORM_STD_FREE",
        # Doc 
        None
    ],
    ["MBEDTLS_PLATFORM_CALLOC_MACRO",
        # Doc 
        None
    ],
    ["MBEDTLS_PLATFORM_FREE_MACRO",
        # Doc 
        None
    ],
]

class KSDKDefineMacros(DefineMacros):
    def __init__(self, o_file):
        super(KSDKDefineMacros, self).__init__()
        self.o_file = o_file
        self._method = "DEFINE"

    def write_platform_memory(self):
        self.write(PLATFORM_MEMORY_DEFINE, "DEFINE")
        self.write(PLATFORM_MEMORY_UNDEFINE, "UNDEFINE")
        self.o_file.write("\n\n#define MBEDTLS_PLATFORM_CALLOC_MACRO SSS_CALLOC")
        self.o_file.write("\n#define MBEDTLS_PLATFORM_FREE_MACRO SSS_FREE\n")


def main():
    o = open(HEADER_FILE, "w")
    macros = KSDKDefineMacros(o)
    o.write(COPYRIGHT)
    o.write(C_HEADER_START)
    o.write("/* Generated by %s */\n\n" %(os.path.basename(__file__)))
    macros.write(DEFINE_MACROS, "DEFINE")
    macros.write(UNDEFINE_MACROS, "UNDEFINE")

    # Write Platform memory macros
    o.write("#include <fsl_sss_types.h>\n\n")
    macros.write_platform_memory()
    macros.undefine_symbol(o, "FD_SETSIZE")
    o.write("#define FD_SETSIZE 1024\n")
    o.write(C_HEADER_END)
    o.close()

if __name__ == "__main__":
    main()
