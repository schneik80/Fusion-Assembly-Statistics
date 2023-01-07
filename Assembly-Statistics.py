#Author-Kevin Schneider and Kris Kaplan, Autodesk Inc.
#Description-Simple Assembly Statistics.

import adsk.core, adsk.fusion, traceback

def run(context):

    ui = None
    try:

        app = adsk.core.Application.get()
        ui  = app.userInterface
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Check a Design document is active.
        if not design:
            ui.messageBox('No active Fusion design', 'No Design')
            return

        # Get the root component of the active design.
        rootComp = design.rootComponent
        
        # Get the document details
        root_name = design.rootComponent.name # Get root component name.
        total_unique = design.allComponents.count - 1 # Get unique components, subtract 1 to remove for root component.
        total_count = rootComp.allOccurrences.count # Get total components.

        # Display the result.
        # Write the results to the TEXT COMMANDS window.
        adsk.core.Application.log(f'{root_name}:')
        adsk.core.Application.log(f'Unique components: {total_unique}')
        adsk.core.Application.log(f'Total components: {total_count}')

        # Display results in a MESSAGE BOX.
        ui.messageBox(f"""
            {total_unique} Unique Components. 
            
            {total_count} Total Components.
            """, f'{root_name} Component Statistics', 0, 2)
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))