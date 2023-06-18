# Python-scripts-AWS
here are a few Python scripts that can help you manage your AWS resources.


IAM_polic cleanup - this script cleans up any misspelled policy names, in this example anything that ends in .json, and removes them. Then the script creates a new policy with the same permission but correctly spells the policy and then attaches it to the role/group.
