from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10_10
import pandas

# read the csv 
df = pandas.read_csv('cars.csv')

# create column data source from data frames
source = ColumnDataSource(df)

output_file('index.html')

# add plot
p = figure(
    y_range = df['Car'],
    outer_width = 800,
    outer_height = 600,
    title = 'Cars with Top HP',
    x_axis_label = 'Horsepower',
    tools = "pan,box_select,zoom_in,zoom_out,save,reset"
)

#  render glyph
p.scatter(
    x = 'Horsepower',
    y = 'Car',
    size = 10,
    fill_color = factor_cmap(
        'Car',
        palette = Category10_10,
        factors = df['Car'].unique()
    ),
    source = source
)

# add legend
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '12px'

# add tool tips
hover = HoverTool()

hover.tooltips = """
    <div>
        <h3>@Car</h3>
        <div><strong>Price: </strong>@Price</div>
        <div><strong>Hp: </strong>@Horsepower</div>
        <div><img src="@Image" alt="" width="200" ></div>
    </div>
"""

p.add_tools(hover)

# show results
show(p)
