/* Copyright 2020 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/* ************************************************************************** */
/* Includes                                                                   */
/* ************************************************************************** */
#ifndef MFA_PROCESS_TST_H_INCLUDED
#define MFA_PROCESS_TST_H_INCLUDED

/* ************************************************************************** */
/* Defines                                                                    */
/* ************************************************************************** */

/* ************************************************************************** */
/* Global Variables                                                           */
/* ************************************************************************** */

/* ************************************************************************** */
/* Structures and Typedefs                                                    */
/* ************************************************************************** */

/* ************************************************************************** */
/* Global Variables                                                           */
/* ************************************************************************** */

/* ************************************************************************** */
/* Function declarations                                                      */
/* ************************************************************************** */

void mfa_process_testapplet(const char *aid, const char *command);
//#if (SMCOM_JRCP_V1) || (SMCOM_JRCP_V2)
//void mfa_process_prepareTear(const char *);
//#endif
void mfa_process_testIoTPreUpgrade();
void mfa_process_testIoTPostUpgrade();

#endif //MFA_PROCESS_TST_H_INCLUDED