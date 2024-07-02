from ak_safe.Enumeration.Units import eUnits, eUnit_dict

def test_inputs_values():
    for k, v in eUnit_dict.items():
        assert eUnits(k) == v
        
    for k, v in eUnit_dict.items():
            assert eUnits(v) == k
            
    for k in eUnit_dict.keys():
        assert eUnits(eUnits(k)) == k
        
    for v in eUnit_dict.values():
        assert eUnits(eUnits(v)) == v