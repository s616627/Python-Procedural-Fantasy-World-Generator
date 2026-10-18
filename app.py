import os
import random
from flask import Flask, render_template, request, url_for, redirect

from WorldGenerator import World

TILE_SIZE = 10

def tile_file(biome):
    return biome.lower().replace(" ","_") + ".PNG"

def static_tile(file_name):
    return url_for("static", filename=f"tiles/{file_name}")

app = Flask(__name__)

def build_tiles(world):
    rows = []
    for y in range(world.height):
        row = []
        for x in range(world.width):
            biome = world.biome_map[y][x]
            loc = world.location_map[y][x]
            is_sea = biome in ("Sea", "Artic Sea")
            city = loc.name if loc.name != "---" else None

            layers = []
            if city:
                layers.append(static_tile("capitol.PNG"))

            layers.append(static_tile(tile_file(biome)))

            row.append({
                "bg": ", ".join(f"url({u})" for u in layers),
                "title": city or biome
            })
        rows.append(row)
    return rows

@app.route("/")
def index():

    seed = int(request.args.get("seed", random.randint(0, 999999)))
    return redirect(url_for("create_from_set_seed", url_seed=seed))

@app.route("/<url_seed>")
def create_from_set_seed(url_seed):
    width = int(request.args.get("w", 170))
    height = int(request.args.get("h", 80))

    random.seed(url_seed)          # same seed -> same world
    world = World(width, height)

    capitols = [(c, r.plural_name) for c, r in zip(world.city_names_list, world.fantasy_races)]

    return render_template(
        "map.html",
        tiles=build_tiles(world),
        width=width, height=height, seed=url_seed,
        tile=TILE_SIZE,
        capitols=capitols,
    )

if __name__ == "__main__":
    app.run(debug=True)