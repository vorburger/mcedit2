"""
    test_longlong_qvariant
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import logging

log = logging.getLogger(__name__)

from PySide import QtGui, QtCore
from PySide.QtCore import Qt

class TestModel(QtCore.QAbstractListModel):
    def rowCount(self, parent=None):
        return 1

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return -(1 << 45)


def main():
    model = TestModel()
    proxyModel = QtGui.QSortFilterProxyModel()
    proxyModel.setSourceModel(model)
    proxyModel.data(proxyModel.index(0, 0, QtCore.QModelIndex()))

if __name__ == '__main__':
    main()