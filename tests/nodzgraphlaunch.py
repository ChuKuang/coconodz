from coconodz import (Nodzgraph,
                      application,
                      Qt
                      )
from coconodz.lib import Backdrop


if __name__ == '__main__':
    # open Nodzgraph standalone
    if application:

        text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

        Nodzgraph.open()
        #Nodzgraph.graph.creation_field.available_items = ["test", "blabla" "backdrop"]
        Nodzgraph.attribute_context.mode = "plug"
        Nodzgraph.attribute_context.available_items = {"blabla":"", "blabla22":""}
        node1 = Nodzgraph.graph.create_node("SimNode", node_type="SimNode")
        node2 = Nodzgraph.graph.create_node("MeshingNode", node_type="MeshingNode")
        node3 = Nodzgraph.graph.create_node("CachingNode", node_type="CachingNode")

        application.exec_()