#!/usr/bin/env python3
"""
GraphQL example using Graphene.

This module defines a simple GraphQL schema with a single query field 'hello'.
"""

import graphene


class Query(graphene.ObjectType):
    """
    Root GraphQL query type.
    
    Fields:
        hello (str): Returns a simple greeting message.
    """
    hello = graphene.String(description="Returns a greeting message")

    def resolve_hello(self, info):
        """
        Resolver for the 'hello' field.

        Args:
            info: GraphQL execution info.

        Returns:
            str: A greeting message.
        """
        return "Hello, GraphQL!"


schema = graphene.Schema(query=Query)
