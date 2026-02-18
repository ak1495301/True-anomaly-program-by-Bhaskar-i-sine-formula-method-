"""THIS MODULE WAS CREATED BY AYUSH KUSHWAHA
This module is to convert different type of anomalies of planet"""


def direct_anomely(o,e):
    """this function directly converts mean anomaly to real anomaly
    it take input as mean_anomaly,eccentricity"""
    import math as m
    from numpy import roots
    pi=m.pi
    if o<pi:
        a=4
        b=(-4 * pi + 16 * e - 4 * o)
        c=(5 * pi * pi - 16 * e * pi + 4 * o * pi)
        d=(-5 * o * pi * pi)
        root=roots([a, b, c, d])
    elif o==2*pi:
        root=[0, 0, pi]
    elif o>=pi:
        a=4
        b=(-4 * o + 16 * e - 12 * pi)
        c=(12 * pi * o - 48 * pi * e + 13 * pi * pi)
        d=(-13 * o * pi * pi + 32 * e * pi * pi)
        root=roots([a, b, c, d])
    for i in root:
        if i.imag==0:
            E=i
            break
        else:
            continue
    E=float(E)
    v = m.acos((m.cos(E) - e) / (1 - e * m.cos(E)))
    if E <= m.pi:
        return v
    elif E > m.pi:
        v = 2 * m.pi - v
    return v
def mean_to_eccentric_anomely(o,e):
    """"
    THis
    module is to
    convert
    mean
    anomaly
    to
    eccentric
    anomaly
    it
    requires
    mean
    anomaly and eccentricity
    """
    import math as m
    from numpy import roots
    pi=m.pi
    if o<pi:
        a=4
        b=(-4 * pi + 16 * e - 4 * o)
        c=(5 * pi * pi - 16 * e * pi + 4 * o * pi)
        d=(-5 * o * pi * pi)
        root=roots([a, b, c, d])
    elif o==2*pi:
        root=[0, 0, pi]
    elif o>=pi:
        a=4
        b=(-4 * o + 16 * e - 12 * pi)
        c=(12 * pi * o - 48 * pi * e + 13 * pi * pi)
        d=(-13 * o * pi * pi + 32 * e * pi * pi)
        root=roots([a, b, c, d])
    for i in root:
        if i.imag==0:
            E=i
            break
        else:
            continue
    return float(E)
def eccentric_to_real_anomaly(E,e):
    """THis module is to convert eccentric anomely to real/True anomaly
    it requires eccentric anomaly and eccentricity"""
    import math as m
    v = m.acos((m.cos(E) - e) / (1 - e * m.cos(E)))
    if E<=m.pi:
        return v
    elif E>m.pi:
        v=2*m.pi-v
    return v


