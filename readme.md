<div class="document">

<div class="documentwrapper">

<div class="bodywrapper">

<div class="body" role="main">

<div class="section" id="welcome-to-simulator-ogame-s-documentation">

# Welcome to simulator_ogame’s documentation![¶](#welcome-to-simulator-ogame-s-documentation "Permalink to this headline")

<span class="target" id="module-Loader"></span>

<dl class="class">

<dt id="Loader.Loader">_class_ `Loader.``Loader`[¶] </dt>

<dd>

class for loading game data from text files

<dl class="staticmethod">

<dt id="Loader.Loader.load_fast_attack_data">_static_ `load_fast_attack_data`<span class="sig-paren">(</span>_shipdata_<span class="sig-paren">)</span>[¶] </dt>

<dd>

loads the ship fast attack data defined in dane_statkow.txt

</dd>

</dl>

<dl class="staticmethod">

<dt id="Loader.Loader.load_fleet">_static_ `load_fleet`<span class="sig-paren">(</span>_shipdata_, _fleetname_<span class="sig-paren">)</span>[¶] </dt>

<dd>

loads the ship data defined in /data/{fleetname}/.txt

</dd>

</dl>

<dl class="staticmethod">

<dt id="Loader.Loader.load_ship_data">_static_ `load_ship_data`<span class="sig-paren">(</span>_shipdata_<span class="sig-paren">)</span>[¶] </dt>

<dd>

loads the ship data defined in dane_statkow.txt

</dd>

</dl>

</dd>

</dl>

<span class="target" id="module-Fleet"></span>

<dl class="class">

<dt id="Fleet.Fleet">_class_ `Fleet.``Fleet`<span class="sig-paren">(</span>_sd_, _name_<span class="sig-paren">)</span>[¶] </dt>

<dd>

class containing basic fleet operations and game related functions

<dl class="method">

<dt id="Fleet.Fleet.attack">`attack`<span class="sig-paren">(</span>_other_<span class="sig-paren">)</span>[¶] </dt>

<dd>

sequenially executes the attack function for each ship on the fleet list

</dd>

</dl>

<dl class="method">

<dt id="Fleet.Fleet.evaluate_fleet">`evaluate_fleet`<span class="sig-paren">(</span><span class="sig-paren">)</span>[¶] </dt>

<dd>

decides to remove or keep sheeps in the fleet, regenerates shields

</dd>

</dl>

<dl class="method">

<dt id="Fleet.Fleet.get_random_target">`get_random_target`<span class="sig-paren">(</span><span class="sig-paren">)</span>[¶] </dt>

<dd>

chooses a random target based on uniform distribution random value

</dd>

</dl>

<dl class="method">

<dt id="Fleet.Fleet.print_fleet">`print_fleet`<span class="sig-paren">(</span><span class="sig-paren">)</span>[¶] </dt>

<dd>

prints the fleet nicely

</dd>

</dl>

</dd>

</dl>

<span class="target" id="module-Ship"></span>

<dl class="class">

<dt id="Ship.Ship">_class_ `Ship.``Ship`<span class="sig-paren">(</span>_shipdata_, _shortname_<span class="sig-paren">)</span>[¶] </dt>

<dd>

Main ship class for all ingame ship types

<dl class="method">

<dt id="Ship.Ship.do_attack">`do_attack`<span class="sig-paren">(</span>_other_<span class="sig-paren">)</span>[¶] </dt>

<dd>

main attack function, @param Ship other

</dd>

</dl>

<dl class="method">

<dt id="Ship.Ship.get_attack_chance">`get_attack_chance`<span class="sig-paren">(</span>_target_shortname_<span class="sig-paren">)</span>[¶] </dt>

<dd>

returns additional attack chance based on the target name

</dd>

</dl>

</dd>

</dl>

<span class="target" id="module-ShipData"></span>

<dl class="class">

<dt id="ShipData.ShipData">_class_ `ShipData.``ShipData`[¶] </dt>

<dd>

class containing ship info it’s meant to be instantiated only once and used throughout the application

<dl class="method">

<dt id="ShipData.ShipData.add_fast_attack_data">`add_fast_attack_data`<span class="sig-paren">(</span>_shortname_, _enemy_, _factor_<span class="sig-paren">)</span>[¶] </dt>

<dd>

adds a loaded fast attack data to the ships dictionary

</dd>

</dl>

<dl class="method">

<dt id="ShipData.ShipData.add_ship_data">`add_ship_data`<span class="sig-paren">(</span>_data_<span class="sig-paren">)</span>[¶] </dt>

<dd>

adds a loaded ship data to the ships dictionary

</dd>

</dl>

<dl class="method">

<dt id="ShipData.ShipData.get_data">`get_data`<span class="sig-paren">(</span>_shortname_<span class="sig-paren">)</span>[¶] </dt>

<dd>

returns ship data from the ship data dictionary

</dd>

</dl>

</dd>

</dl>

</div>

<div class="section" id="indices-and-tables">

# Indices and tables[¶](#indices-and-tables "Permalink to this headline")

*   [<span class="std std-ref">Index</span>](genindex.html)
*   [<span class="std std-ref">Module Index</span>](py-modindex.html)
*   [<span class="std std-ref">Search Page</span>](search.html)

</div>

</div>

</div>

</div>

<div class="sphinxsidebar" role="navigation" aria-label="main navigation">

<div class="sphinxsidebarwrapper">

<div class="relations">

### Related Topics

*   [Documentation overview](index.html#document-index)

</div>

</div>

</div>

</div>

<div class="footer">©2017, pablo. | Powered by [Sphinx 1.6.5](http://sphinx-doc.org/) & [Alabaster 0.7.10](https://github.com/bitprophet/alabaster)</div>
