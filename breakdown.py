import json

with open('packages.json') as f:
    data = json.load(f)
    
count_deps = 0
ordered_deps = []

for i,v in enumerate(data):
    if i % 2 == 0:
        v['owner'] = 'fernandoataoldotcom'
    else:
        v['owner'] = 'venkatamutyala' 
    count_deps += len(v['dependencies'])
    sorted_keys = sorted(v.keys(), reverse=True)
    ordered_deps.append({key: v[key] for key in sorted_keys})
    
v_count = 0
a_count = 0
missing = 0

for i in ordered_deps:
    if i['owner'] == 'venkatamutyala':
        v_count += len(i['dependencies'])
    elif i['owner'] == 'fernandoataoldotcom':
        a_count += len(i['dependencies'])
    else:
        missing += len(i['dependencies'])

print(ordered_deps)
print(f'\ntotal dependent repositories: {count_deps}')
print(f'total external dependencies: {len(data)}')

print(f'venkatamutyala dependent repositories: {v_count}')
print(f'fernandoataoldotcom dependent repositories: {a_count}')
print(f'missing: {missing}')
