import weakref #The weakref module allows the Python programmer to create weak references to objects.
#https://docs.python.org/3/library/weakref.html

'''
To avoid any type of Circular dependency/import this module is created 
'''

OBJ_MAP = {
    
}

_id2obj_dict = weakref.WeakValueDictionary()

def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid




def id2obj(oid):
    return _id2obj_dict[oid]




"""
The problem with circular dependencies is rather like the chicken and egg problem.

If you depend on me setting something up, and I depend on you setting something up, how do we start?

The corollary of this is how do we end - if I have a reference to your resource and you have a reference to mine, 
I can never clean up because that would break you, and you cannot clean up because that would break me.

The answer in both cases is to introduce a middleman, passing the dependency from one of the parties to him, 
So if you passed your resource on to the middleman, you would depend on me and the middleman, and I would depend 
on the middleman. Thus you can clean up because you now hold no resource, and I can clean up 
because no-one depends on me, and then the middleman can clean up.
Ref: https://stackoverflow.com/questions/26804803/is-circular-dependency-good-or-bad
"""
