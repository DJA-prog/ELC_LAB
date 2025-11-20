#!/usr/bin/env python3
"""
Sample data script to populate the database with initial components and categories
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from component_manager import DatabaseManager


def populate_sample_data():
    """Populate the database with sample electronic components and categories"""
    db = DatabaseManager()
    
    print("Adding sample categories...")
    
    # Add categories
    categories_data = [
        ("RESISTOR", "Fixed resistors and variable resistors"),
        ("CAPACITOR", "Electrolytic, ceramic, and other capacitors"),
        ("DIODE", "LEDs, rectifier diodes, Zener diodes"),
        ("IC", "Integrated circuits and microcontrollers"),
        ("TRANSISTOR", "BJTs, MOSFETs, and other transistors"),
        ("INDUCTOR", "Coils and transformers"),
        ("CONNECTOR", "Terminal blocks, headers, and connectors"),
        ("SWITCH", "Push buttons, toggle switches"),
        ("SENSOR", "Temperature, pressure, and other sensors"),
        ("POWER", "Power supplies and voltage regulators")
    ]
    
    category_ids = {}
    for name, desc in categories_data:
        cat_id = db.insert_category(name, desc)
        category_ids[name] = cat_id
        print(f"Added category: {name} (ID: {cat_id})")
    
    print("\nAdding sample components...")
    
    # Add components
    components_data = [
        ("22nF", "22nF Ceramic Capacitor", 0.23),
        ("10mH", "10mH Inductor", 0.27),
        ("1uH", "1uH Inductor", 0.25),
        ("LED-RED", "Red LED 5mm", 0.74),
        ("LM317", "LM317 Voltage Regulator IC", 0.44),
        ("LM741", "LM741 Op-Amp IC", 4.50),
        ("MC34063", "MC34063 Switching Regulator IC", 27.50),
        ("IRFZ44", "IRFZ44 N-Channel MOSFET", 3.40),
        ("T-BLOCK-2", "2-pin Terminal Block", 3.24),
        ("T-BLOCK-3", "3-pin Terminal Block", 3.54),
        ("SW-PUSH", "Push Button Switch", 13.50),
        ("RES-1K", "1kΩ Resistor 1/4W", 0.05),
        ("RES-10K", "10kΩ Resistor 1/4W", 0.05),
        ("CAP-100uF", "100μF Electrolytic Capacitor", 0.35),
        ("DIODE-1N4007", "1N4007 Rectifier Diode", 0.12)
    ]
    
    component_ids = {}
    for identifier, desc, price in components_data:
        comp_id = db.insert_component(identifier, desc, price)
        component_ids[identifier] = comp_id
        print(f"Added component: {identifier} (ID: {comp_id})")
    
    print("\nCreating component-category links...")
    
    # Create links based on component types
    links = [
        ("22nF", "CAPACITOR"),
        ("10mH", "INDUCTOR"),
        ("1uH", "INDUCTOR"),
        ("LED-RED", "DIODE"),
        ("LM317", "IC"),
        ("LM317", "POWER"),
        ("LM741", "IC"),
        ("MC34063", "IC"),
        ("MC34063", "POWER"),
        ("IRFZ44", "TRANSISTOR"),
        ("T-BLOCK-2", "CONNECTOR"),
        ("T-BLOCK-3", "CONNECTOR"),
        ("SW-PUSH", "SWITCH"),
        ("RES-1K", "RESISTOR"),
        ("RES-10K", "RESISTOR"),
        ("CAP-100uF", "CAPACITOR"),
        ("DIODE-1N4007", "DIODE")
    ]
    
    for comp_name, cat_name in links:
        if comp_name in component_ids and cat_name in category_ids:
            comp_id = component_ids[comp_name]
            cat_id = category_ids[cat_name]
            db.link_component_category(comp_id, cat_id)
            print(f"Linked {comp_name} to {cat_name}")
    
    print("\nSample data populated successfully!")
    print(f"Added {len(categories_data)} categories")
    print(f"Added {len(components_data)} components")
    print(f"Created {len(links)} links")


if __name__ == '__main__':
    populate_sample_data()