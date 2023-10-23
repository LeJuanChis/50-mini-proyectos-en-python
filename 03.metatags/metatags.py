import json
import metadata_parser


url = ''

page = metadata_parser.MetadataParser(url)


json_formatted = json.dumps(page.metadata, indent=4)

print(json_formatted)
