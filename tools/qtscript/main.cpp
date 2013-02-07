#include "QsEnv.hpp"
#include <iostream>
#include <QtGui/QApplication>
#include "QmlAdapter.hpp"

using namespace QsExecute;

namespace QsExecute {

static int usage(int, char *argv[])
{
    qDebug() << argv[0] << " <script_name>";
    return 0;
}

int executeScript(int argc, char *argv[])
{
    QCoreApplication app(argc, argv);
    if (app.arguments().size() < 2)
        return usage(argc, argv);

    QString script_file(app.arguments().at(1));

    QScriptEngine engine;
    auto script_env = loadEnv(app, engine);
    int rc = EXIT_SUCCESS;

    try {
        auto res = script_env->load(script_file);
        if (engine.hasUncaughtException()
            && engine.uncaughtException().isValid())
            rc = EXIT_FAILURE;
    } catch (Error const &e) {
        qDebug() << "Failed to eval:" << script_file;
        qDebug() << e.msg;
        rc = EXIT_FAILURE;
    }
    return rc == EXIT_SUCCESS && script_env->shouldWait()
        ? app.exec() : rc;
}

int executeDeclarative(int argc, char *argv[])
{
    QApplication app(argc, argv);
    if (app.arguments().size() < 2)
        return usage(argc, argv);
    QString script_file(app.arguments().at(1));

    QDeclarativeView view;

    setupDeclarative(app, view, QFileInfo(script_file).absoluteFilePath());
    view.setSource(QUrl::fromLocalFile(script_file));

    view.setAttribute(Qt::WA_OpaquePaintEvent);
    view.setAttribute(Qt::WA_NoSystemBackground);
    view.viewport()->setAttribute(Qt::WA_OpaquePaintEvent);
    view.viewport()->setAttribute(Qt::WA_NoSystemBackground);

    view.showFullScreen();
    return app.exec();
}

}


int main(int argc, char *argv[])
{
    using namespace QsExecute;
    if (argc < 2)
        return usage(argc, argv);

    QString script_file(argv[1]);
    
    if (QFileInfo(script_file).suffix() == "qml") {
        return executeDeclarative(argc, argv);
    } else {
        return executeScript(argc, argv);
    }
}
