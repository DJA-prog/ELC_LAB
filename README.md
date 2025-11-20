# Electronic Component Manager

A Qt5-based desktop application for managing electronic components, categories, and their relationships.

## Features

- **Component Management**: Add, edit, delete, and view electronic components with identifier, description, and price
- **Category Management**: Create and manage component categories
- **Linking System**: Link components to multiple categories and view relationships
- **CSV Import**: Import components from CSV files with intelligent duplicate handling
- **Advanced UI**: Improved layout with table sorting and context menus
- **Database Integration**: SQLite database for persistent storage
- **User-Friendly Interface**: Tabbed interface with intuitive forms and tables

## Installation

1. Ensure you have Python 3.6+ installed
2. Install required dependencies:
   ```bash
   pip install PyQt5
   ```

## Usage

### Running the Application

1. **Run the main application**:
   ```bash
   python component_manager.py
   ```
   
   Or use the launcher script:
   ```bash
   python run_manager.py
   ```

2. **Populate with sample data** (optional):
   ```bash
   python populate_sample_data.py
   ```

### Using the Interface

#### Components Tab
- **Layout**: Component details form at the top, components list below with more space
- **Add Component**: Fill in the identifier (required), description, and price, then click "Add Component"
- **Edit Component**: 
  - **Method 1**: Click on a component in the table to select it, modify the fields, button changes to "Update Component"
  - **Method 2**: Right-click on any component row and select "Edit Component" from the context menu
- **Delete Component**: 
  - **Method 1**: Select a component and click "Delete Component" button
  - **Method 2**: Right-click on any component row and select "Delete Component" from the context menu
- **Table Sorting**: Click on any column header to sort the components by that column (ID, Identifier, Description, Price, Updated)
- **Import CSV**: Click "Import CSV" to import components from a CSV file with columns: ITEM, PRICE, DESCRIPTION
- **Clear Form**: Reset all input fields and return to "Add" mode

##### CSV Import Rules
When importing CSV files:
- **New components**: Always imported regardless of whether they have descriptions
- **Duplicate components** (same identifier) are handled as follows:
  - **Higher price wins**: If the CSV component has a higher price, it overwrites the existing component
  - **Same price with description**: If prices are equal, the component with a description is preferred over one without
  - **Lower price**: If the CSV component has a lower price, the existing component is kept unchanged

#### Categories Tab
- **Add Category**: Enter a category name (required) and description, then click "Add Category"
- **Edit Category**: Select a category from the table, modify the fields, then click "Update Category"
- **Delete Category**: Select a category and click "Delete Category"

#### Link Components & Categories Tab
- **Create Links**: Select a component and category from the dropdown menus, then click "Link"
- **Remove Links**: Select a component and category, then click "Unlink"
- **View Relationships**: 
  - Left panel shows categories for a selected component
  - Right panel shows components for a selected category

## Database Schema

The application uses SQLite with three main tables:

- **components**: Stores component information (id, identifier, description, price, timestamps)
- **categories**: Stores category information (id, name, description, timestamps)
- **component_category**: Junction table for many-to-many relationships

## File Structure

- `component_manager.py` - Main application file with GUI and CSV import
- `run_manager.py` - Launcher script
- `import_csv.py` - Standalone CSV import tool
- `populate_sample_data.py` - Script to add sample data
- `test_csv_import.py` - Test script for CSV import functionality
- `create_dbs.py` - Original database creation script
- `components_users.db` - SQLite database file (created automatically)
- `imports/` - Directory for CSV files to import

## Features in Detail

### Component Management
- Unique identifiers for easy reference
- Rich text descriptions
- Decimal pricing with currency formatting
- Automatic timestamp tracking

### Category System
- Hierarchical organization
- Flexible categorization (components can belong to multiple categories)
- Quick filtering and browsing

### Linking Interface
- Visual representation of relationships
- Easy link creation and removal
- Real-time updates across all views

### Interface Improvements
- **Improved Components Layout**: Form at top, table below with maximum space utilization
- **Table Sorting**: Click column headers to sort by ID, Identifier, Description, Price, or Update date
- **Context Menus**: Right-click on any component for quick Edit/Delete actions
- **Smart Button Behavior**: Single "Add Component" button that becomes "Update Component" when editing
- **Enhanced Navigation**: Streamlined workflow for component management

## Tips

1. **Backup your database**: The SQLite file `components_users.db` contains all your data
2. **Use clear identifiers**: Component identifiers should be unique and descriptive
3. **Organize categories**: Plan your category structure before adding many components
4. **CSV Import**: Prepare CSV files with columns: ITEM, PRICE, DESCRIPTION for bulk imports
5. **Regular updates**: Keep component prices and descriptions current

### CSV Import Tips

1. **File Format**: Use CSV format with headers: ITEM, PRICE, DESCRIPTION
2. **New Components**: All new components are imported, with or without descriptions
3. **Duplicates**: Higher prices overwrite existing components; equal prices prefer descriptions
4. **Validation**: Empty rows and invalid data are automatically skipped
5. **Batch Operations**: Use CSV import for adding many components at once

## Command Line Tools

### Standalone CSV Import
```bash
python import_csv.py [path_to_csv_file]
```

### Test Import Functionality
```bash
python test_csv_import.py
```

## Troubleshooting

### Common Issues

1. **PyQt5 not found**: Install PyQt5 using `pip install PyQt5`
2. **Database locked**: Close all instances of the application before restarting
3. **Permission errors**: Ensure you have write permissions in the application directory

### Getting Help

- Check the console output for error messages
- Ensure all required dependencies are installed
- Verify that the database file is not corrupted

## Sample Data

Run `populate_sample_data.py` to add sample electronic components including:
- Resistors, capacitors, inductors
- LEDs and diodes  
- Integrated circuits (LM317, LM741, MC34063)
- Transistors and MOSFETs
- Terminal blocks and switches

This sample data demonstrates the full functionality of the application and provides a starting point for your own component inventory.