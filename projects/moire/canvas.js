function layerDraw()
{
    var canvas = document.querySelector('#moireCanvas'),
        ctx = canvas.getContext('2d'),
        height = canvas.clientHeight,
        width = canvas.clientWidth,
        size = Number(document.querySelector('#size-control').value),
        r = Number(document.querySelector('#rotate').value)/180,
        x = Number(document.querySelector('#shiftx').value),
        y = Number(document.querySelector('#shifty').value);
    ctx.beginPath();


    for(i=0; i<Math.floor(height/size); i++){
        var x_backup = x;
        var y_backup = y;
        ctx.moveTo(x + size * Math.cos(r*Math.PI), y + size * Math.sin(r*Math.PI));
        for (j=0; j<Math.floor(width/size); j++){
            for (side=1; side < 5; side++) {
              ctx.lineTo(x + size * Math.cos(side *  Math.PI / 3 + r*Math.PI), y + size * Math.sin(side *  Math.PI / 3 + r*Math.PI));
            }
            ctx.moveTo(x + size * Math.cos(side * 2 * Math.PI / 6 + r*Math.PI), y + size * Math.sin(side * 2 * Math.PI / 6 + r*Math.PI));
            side += 1;
            ctx.lineTo(x + size * Math.cos(side * 2 * Math.PI / 6 + r*Math.PI), y + size * Math.sin(side * 2 * Math.PI / 6 + r*Math.PI));
            ctx.lineTo(x + 2 * size * Math.cos(r*Math.PI), y + size * Math.sin(r*Math.PI));
            x += 3*size*Math.cos(r*Math.PI);
            y += 3*size*Math.sin(r*Math.PI);
            ctx.moveTo(x + size * Math.cos(r*Math.PI), y + size * Math.sin(r*Math.PI));
        }
        x = x_backup + 2*size*Math.cos(Math.PI/6)*Math.sin(Math.PI*r);
        y = y_backup + 2*size*Math.cos(Math.PI/6)*Math.cos(Math.PI*r);
    }

    ctx.stroke()
}

