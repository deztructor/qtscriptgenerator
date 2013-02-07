import QtQuick 1.1
import Mer.QtScript 1.1

Rectangle
{
    id : main
    width : 300
    height: 300
    QtScriptActor {
        id : actor
        source : "actor.js"
        onError : {
            console.log("ERR:")
            for (var n in error)
                console.log(n, error[n])
        }
    }

    Component.onCompleted : {
        data.append({ name: "before", value : "first item"})
        data.append({ name: "click items while", value : "loading" })
        actor.send({ from_qml : "qml data"}, function (reply) {
            for (var n in reply)
                data.append({ name: n, value : reply[n] })
        })
        data.append({ name: "after message", value : "more items to follow" })
    }

    ListModel {
        id: data
        ListElement {
            name : "initial"
            value: 1
        }
        ListElement {
            name : "initial"
            value: 2
        }
    }

    ListView {
        anchors { fill: parent }
        model : data
        delegate : TestItem {
            id: txt
            text: model.name + " " + model.value
        }
    }

}
