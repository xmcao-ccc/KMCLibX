""" Module for holding common printing utility functions. """


# Copyright (c)  2013-2014  Mikael Leetmaa
# Copyright (c)  2016-2019  Shao Zhengjiang
#
# This file is part of the KMCLibX project(based on KMCLib) distributed under the terms of the
# GNU General Public License version 3, see <http://www.gnu.org/licenses/>.
#


import sys

from ..Backend.Backend import MPICommons
from .. import __version__
from .. import __copyright__
from .. import __email__
from .. import __license__
from .. import __author__


def prettyPrint(msg, output=None):
    """
    Utility function for printing an output string to screen.

    :param msg: The message to print.
    :type msg: str

    :param out: The stream to write to. Defaults to sys.stdout.
    """
    # Set the default.
    if output is None:
        output = sys.stdout

    # Write.
    if MPICommons.isMaster():
        output.write(msg)
        output.write("\n")
    MPICommons.barrier()


def printHeader(output=None):
    """
    Utility function for printing the run header information.

    :param out: The stream to write to. Defaults to sys.stdout.
    """
    # Set the default.
    if output is None:
        output = sys.stdout

    # Write.
    prettyPrint("# -----------------------------------------------------------------------------", output)
    prettyPrint("# KMCLibX version " + __version__, output)
    prettyPrint("# Distributed under the " + __license__ + " license", output)
    prettyPrint("# " + __copyright__, output)
    prettyPrint("# Developed by " + __author__ + " <" + __email__ + ">", output)
    prettyPrint("#", output)
    prettyPrint("# KMCLibX is developed based on KMCLib (https://github.com/leetmaa/KMCLib)", output)
    prettyPrint("# Developed by Mikael Leetmaa <leetmaa@kth.se>", output)

    prettyPrint("#", output)
    prettyPrint("# This program is distributed in the hope that it will be useful", output)
    prettyPrint("# but WITHOUT ANY WARRANTY; without even the implied warranty of", output)
    prettyPrint("# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the", output)
    prettyPrint("# LICENSE and README files, and the source code, for details.", output)
    prettyPrint("#", output)
    prettyPrint("# You should have received a copy of the GNU General Public License version 3", output)
    prettyPrint("# (GPLv3) along with this program. If not, see <http://www.gnu.org/licenses/>.", output)
    prettyPrint("# -----------------------------------------------------------------------------", output)
    prettyPrint("", output)
