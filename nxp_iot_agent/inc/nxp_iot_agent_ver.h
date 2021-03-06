/* Copyright 2019-2021 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 *
 */

#ifndef NXP_IOT_AGENT_VERSION_INFO_H_INCLUDED
#define NXP_IOT_AGENT_VERSION_INFO_H_INCLUDED


/* clang-format off */
#define NXP_IOT_AGENT_PROD_NAME          "nxp_iot_agent"
#define NXP_IOT_AGENT_VER_STRING_NUM     "v03.03.00_20210628"
#define NXP_IOT_AGENT_PROD_NAME_VER_FULL "nxp_iot_agent_v03.03.00_20210628"
#define NXP_IOT_AGENT_VER_MAJOR          (3u)
#define NXP_IOT_AGENT_VER_MINOR          (3u)
#define NXP_IOT_AGENT_VER_DEV            (0u)

/* v03.03 = 30003u */
#define NXP_IOT_AGENT_VER_MAJOR_MINOR ( 0 \
    | (NXP_IOT_AGENT_VER_MAJOR * 10000u)    \
    | (NXP_IOT_AGENT_VER_MINOR))

/* v03.03.00 = 300030000ULL */
#define NXP_IOT_AGENT_VER_MAJOR_MINOR_DEV ( 0 \
    | (NXP_IOT_AGENT_VER_MAJOR * 10000*10000u)    \
    | (NXP_IOT_AGENT_VER_MINOR * 10000u)    \
    | (NXP_IOT_AGENT_VER_DEV))

/* clang-format on */


/* Version Information:
 * Generated by:
 *     scripts\version_info.py (v2019.01.17_00)
 *
 * Do not edit this file. Update:
 *     nxp_iot_agent/version_info.txt instead.
 *
 *
 * prod_name = "nxp_iot_agent"
 *
 * prod_desc = "EdgeLock 2GO agent"
 *
 * lang_c_prefix = prod_name.upper()
 *
 * lang_namespace = ""
 *
 * v_major  = "03"
 *
 * v_minor  = "03"
 *
 * v_dev    = "00"
 *
 * v_meta   = ""
 *
 * maturity = "B"
 *
 */

#endif /* NXP_IOT_AGENT_VERSION_INFO_H_INCLUDED */
