greaterThan(QT_MAJOR_VERSION, 4): QT += widgets
TARGET = qtscript_gui
include(../qtbindingsbase.pri)

SOURCES += $$GENERATEDCPP/com_trolltech_qt_gui/plugin.cpp
HEADERS += fontprivate.h

include($$GENERATEDCPP/com_trolltech_qt_gui/com_trolltech_qt_gui.pri)
