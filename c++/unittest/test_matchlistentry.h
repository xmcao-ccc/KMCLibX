/*
  Copyright (c)  2012-2013  Mikael Leetmaa

  This file is part of the KMCLib project distributed under the terms of the
  GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
*/


#ifndef __TEST_MATCHLISTENTRY__
#define __TEST_MATCHLISTENTRY__

#include <iostream>
#include <string>

#include <cppunit/TestCase.h>
#include <cppunit/TestSuite.h>
#include <cppunit/TestCaller.h>
#include <cppunit/TestRunner.h>

#include <cppunit/extensions/HelperMacros.h>

class Test_MatchListEntry : public CppUnit::TestCase {

public:

    CPPUNIT_TEST_SUITE( Test_MatchListEntry );
    CPPUNIT_TEST( testMinimalMatchListEntryConstruction );
    CPPUNIT_TEST( testMinimalMatchListEntryNotEqualOperator );
    CPPUNIT_TEST( testMinimalMatchListEntryLessOperator );
    CPPUNIT_TEST( testMinimalMatchListEntryEqualOperator );
    CPPUNIT_TEST( testProcessMatchListEntryConstruction );
    CPPUNIT_TEST( testConfigMatchListEntryConstruction );
    CPPUNIT_TEST_SUITE_END();

    void testMinimalMatchListEntryConstruction();
    void testMinimalMatchListEntryNotEqualOperator();
    void testMinimalMatchListEntryLessOperator();
    void testMinimalMatchListEntryEqualOperator(); 
    void testProcessMatchListEntryConstruction();
    void testConfigMatchListEntryConstruction();

};

#endif  // __TEST_MATCHLISTENTRY__

