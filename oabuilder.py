import oapackage


def build_oa(levels, factors, strength, index):
    arrayclass = oapackage.arraydata_t(levels, index * (levels ** strength), strength, factors)
    arrayclass.complete_arraydata()
    al = arrayclass.create_root()
    for i in range(factors - strength):
        al = oapackage.extend_array(al, arrayclass)[0]
    return al.getarray()
