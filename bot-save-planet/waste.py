def sort_waste(type_waste):
    waste = {
        "plastico": {
            "reciclar": ["botellas de agua", "envases de alimentos", "tapas"],
            "basura": ["plásticos mezclados con comida", "utensilios desechables sucios"]
        },
        "papel": {
            "reciclar": ["revistas", "hojas impresas", "cajas de cartón limpias"],
            "basura": ["papel higiénico usado", "servilletas sucias"]
        },
        "vidrio": {
            "reciclar": ["botellas de vidrio", "tarros", "frascos"],
            "basura": ["vidrio roto contaminado con químicos", "espejos rotos"]
        },
        "orgánico": {
            "reciclar": ["cáscaras de frutas", "restos de vegetales", "posos de café (compostaje)"],
            "basura": ["huesos grandes", "residuos cocinados en exceso de grasa"]
        },
        "metal": {
            "reciclar": ["latas de aluminio", "tapas de metal", "utensilios metálicos limpios"],
            "basura": ["metales oxidados o muy dañados"]
        },
        "otros": {
            "basura": ["pilas comunes", "pañales desechables", "bombillas"]
        }
    }
    #Normalizar la entrada de datos del usuario
    type_waste = type_waste.lower()
    
    if type_waste in waste:
        info = waste[type_waste]
        re = " ".join(info.get("reciclar", []))
        trash =  " ".join(info.get("basura", []))
        
        return (
            f"Tipo de residuo: {type_waste}\n"
            f" -Objetos para reciclar: {re}\n"
            f" -Objetos para tirar a la basura: {trash}\n"
        )
    else:
        return "Lo siento, no reconozco ese tipo de residuo. Por favor, intenta con otro tipo (plástico, papel, vidrio, orgánico, metal, otros)."
        
 
