def isIso(s, t):
    s_d = {}
    t_d = {}
    for i in range(len(s)):
        if s[i] in s_d.keys() and s_d[s[i]] != t[i]:
            return False
        if t[i] in t_d.keys() and t_d[t[i]] != s[i]:
            return False
        s_d[s[i]] = t[i]
        t_d[t[i]] = s[i]
    return True
