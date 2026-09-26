# kestra-jev

## Français

Flow importable qui produit `route` et `probability` via une tâche Python.

Importez `flow.yaml`, créez le secret Kestra `JEV_API_KEY` et fournissez les trois entrées. Le worker doit prendre en charge Docker.

## English

Importable flow producing `route` and `probability` via a Python task.

Import `flow.yaml`, configure Kestra secret `JEV_API_KEY`, and run with `content`, `question`, `threshold`. The Python task uses a Docker task runner and `ghcr.io/kestra-io/kestrapy:latest`; configure Docker availability on your worker. Outputs are `outputs.decide.vars.route` and `outputs.decide.vars.probability`.

## Español

Flujo importable que produce `route` y `probability` mediante una tarea Python.

Importe `flow.yaml`, cree el secreto Kestra `JEV_API_KEY` y proporcione las tres entradas. El worker debe admitir Docker.

## Contract / Contrat / Contrato

`yes`, `no`, `review`, `failure`; threshold default `0.8`. `review` is a real undecided state. Empty or oversized input becomes `review`; transport or invalid-response errors become `failure`. The shared client caps input at 32 KiB, response at 100 KiB, timeout at 10 s and calls at 10,000 per process; YAML templates enforce their own input and response bounds. No raw input is logged by this project. User data goes to the TypeSafe Jev API.

FR : `review` exige une revue humaine ; `failure` signale une erreur. Le contenu est envoyé à l’API TypeSafe Jev.

ES: `review` requiere revisión humana; `failure` indica un error. El contenido se envía a la API TypeSafe Jev.

## Development / Développement / Desarrollo

`python -m unittest discover -p "test_*.py" -v`

Platform / Plateforme / Plataforma: [Kestra documentation](https://kestra.io/plugins/plugin-script-python/io.kestra.plugin.scripts.python.commands).

MIT license. Community project; not an official Kestra integration.
