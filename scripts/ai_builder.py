import argparse
import os
import xml.etree.ElementTree as ET

def parse_arguments():
    parser = argparse.ArgumentParser(description="MasterAppFactoryV3 Core AI Orchestrator")
    parser.add_argument('--name', type=str, required=True, help="Target Android App Name")
    parser.add_argument('--prompt', type=str, required=True, help="AI Gen prompt instructions")
    return parser.parse_args()

def update_app_name(app_name):
    """
    Modifies strings.xml to dynamically apply the requested app name.
    """
    strings_path = os.path.join('android-template', 'app', 'src', 'main', 'res', 'values', 'strings.xml')
    print(f"[*] Updating application name to '{app_name}' inside {strings_path}...")
    
    if os.path.exists(strings_path):
        tree = ET.parse(strings_path)
        root = tree.getroot()
        
        # Search for <string name="app_name">
        for string_tag in root.findall('string'):
            if string_tag.get('name') == 'app_name':
                string_tag.text = app_name
                break
                
        tree.write(strings_path, encoding='utf-8', xml_declaration=True)
        print("[+] Application name injection completed successfully.")
    else:
        print(f"[-] Error: Could not find strings.xml at {strings_path}")

def main():
    args = parse_arguments()
    print("=========================================")
    print("      MASTER APP FACTORY V3 ENGINE       ")
    print("=========================================")
    print(f"[->] Received Target App Name : {args.name}")
    print(f"[->] Received Execution Prompt : {args.prompt}")
    
    # Run modifications
    update_app_name(args.name)
    
    print("[*] Foundation adjustments done. Handing execution back to Gradle build pipeline...")
    print("=========================================")

if __name__ == '__main__':
    main()
