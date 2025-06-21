# Inverter Subcircuit for SPICE Netlists

This directory contains SPICE netlist files with a reusable inverter subcircuit definition.

## Files

1. **`inverter_subcircuit.net`** - The main subcircuit definition
2. **`inverter_test.net`** - Simple test circuit using the subcircuit
3. **`inverter_chain.net`** - Example with multiple inverters in a chain
4. **`README_inverter_subcircuit.md`** - This documentation file

## Inverter Subcircuit Definition

The inverter subcircuit is defined in `inverter_subcircuit.net`:

```spice
.subckt inverter in out vdd gnd Wp=0.9u Wn=0.3u L=0.2u
M1 out in vdd vdd cmosp W={Wp} L={L}
M2 out in gnd gnd cmosn W={Wn} L={L}
.ends inverter
```

### Parameters

- **in**: Input signal
- **out**: Output signal  
- **vdd**: Power supply (1.8V)
- **gnd**: Ground (0V)
- **Wp**: PMOS transistor width (default: 0.9μm)
- **Wn**: NMOS transistor width (default: 0.3μm)
- **L**: Channel length (default: 0.2μm)

## Usage Examples

### Basic Usage

To instantiate a single inverter:

```spice
X1 in out vdd 0 inverter Wp=0.9u Wn=0.3u L=0.2u
```

### Multiple Inverters

To create a chain of inverters with different configurations:

```spice
* Standard inverter
X1 in out1 vdd 0 inverter Wp=0.9u Wn=0.3u L=0.2u

* Inverter with larger PMOS for better rise time
X2 out1 out2 vdd 0 inverter Wp=1.8u Wn=0.3u L=0.2u

* Inverter with larger NMOS for better fall time
X3 out2 out3 vdd 0 inverter Wp=0.9u Wn=0.6u L=0.2u
```

## Running Simulations

### Prerequisites

1. Ngspice or similar SPICE simulator
2. TSMC 0.18μm technology models (`tsmc18.sp`)

### Running the Test Circuit

```bash
ngspice inverter_test.net
```

### Running the Inverter Chain

```bash
ngspice inverter_chain.net
```

## Design Considerations

### Transistor Sizing

- **PMOS width (Wp)**: Affects rise time and pull-up strength
- **NMOS width (Wn)**: Affects fall time and pull-down strength
- **Typical ratio**: Wp/Wn = 2-3 for balanced rise/fall times

### Common Configurations

1. **Standard inverter**: Wp=0.9u, Wn=0.3u (ratio = 3:1)
2. **Fast rise time**: Wp=1.8u, Wn=0.3u (ratio = 6:1)
3. **Fast fall time**: Wp=0.9u, Wn=0.6u (ratio = 1.5:1)
4. **Balanced**: Wp=0.6u, Wn=0.3u (ratio = 2:1)

### Performance Metrics

The test circuits include measurements for:
- **tphl**: Propagation delay high-to-low (input rising, output falling)
- **tplh**: Propagation delay low-to-high (input falling, output rising)
- **Total delay**: End-to-end delay through inverter chains

## Integration with Other Circuits

To use this inverter subcircuit in your own designs:

1. Include the subcircuit definition:
   ```spice
   .incl inverter_subcircuit.net
   ```

2. Instantiate inverters as needed:
   ```spice
   X1 input output vdd 0 inverter Wp=0.9u Wn=0.3u L=0.2u
   ```

3. Ensure the TSMC models are available:
   ```spice
   .incl tsmc18.sp
   ```

## Troubleshooting

### Common Issues

1. **Model not found**: Ensure `tsmc18.sp` is in the same directory or specify the correct path
2. **Subcircuit not found**: Check that `inverter_subcircuit.net` is properly included
3. **Simulation errors**: Verify all node connections and parameter values

### Parameter Ranges

- **Wp, Wn**: 0.1u to 10u (typical range)
- **L**: 0.18u to 1u (technology dependent)
- **VDD**: 1.8V (for TSMC 0.18μm process) 