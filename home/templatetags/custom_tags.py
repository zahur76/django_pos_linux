from django import template

register = template.Library()


def make_list(value):
    return value.split(",")


register.filter("make_list", make_list)
