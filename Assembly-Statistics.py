#Author-Kevin Schneider and Kris Kaplan, Autodesk Inc.
#Description-Simple Assembly Statistics.

import adsk.core, adsk.fusion, traceback, re

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
        mTitle = f'{root_name} Component Statistics'

        # Display the result.
        # Write the results to the TEXT COMMANDS window.
        adsk.core.Application.log(f'{root_name}:')
        adsk.core.Application.log(f'Unique components: {total_unique}')
        adsk.core.Application.log(f'Total components: {total_count}')

        pattern = r'.[a-zA-Z]\.+\D|\d\.+\D' # match the text commands number/text list output
        stats = app.executeTextCommand("Component.AnalyseHierarchy")
        statsListSplit = stats.splitlines() # split output into a list
        statsList = [re.sub(pattern, '', e) for e in statsListSplit] # strip list numbering from list
        resultString = (
            f"{statsList[1]} <br>"
            f"{statsList[2]} <br>"
            f"Total number of unique components: {total_unique} <br>"
            f"{statsList[3]} <br>"
            f"<br>"
            f"<b>Joint Information:</b><br>"
            f" - {statsList[4]} <br>"
            f" - {statsList[5]} <br>"
            f" - {statsList[6]} <br>"
            f" - {statsList[7]} <br>"
            f" - {statsList[8]} <br>"
            f" - {statsList[9]} <br>"
            f" - {statsList[10]} <br>"
            f" - {statsList[11]} <br>"
            f" - {statsList[12]} <br>"
            f" - {statsList[13]} <br>"
            f" - {statsList[14]} <br>"
            f" - {statsList[15]} <br>"
            f" - {statsList[16]} <br>"
        )

        # Display results in a MESSAGE BOX.
        ui.messageBox(resultString, mTitle, 0, 2)  

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))