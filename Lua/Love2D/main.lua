



function love.load()
  -- love.window.setMode(500, 300)
  button = {}
  button.x = 200
  button.y = 200
  button.radius = 30

  score = 0
  gameFont = love.graphics.newFont(35)
end

function love.update(dt)

end

function love.draw()
  love.graphics.setBackgroundColor(179/255, 217/255, 255/255)

  love.graphics.setColor(77/255, 77/255, 255/255)
  love.graphics.circle("fill", button.x, button.y, button.radius)

  love.graphics.setFont(gameFont)
  love.graphics.setColor(0, 0, 0)
  love.graphics.print("score: " .. score, 50, 50)
end

function love.mousepressed(x, y, leftClick, isTouch)
  if leftClick == 1 then
    if getDistance(button.x, button.y, love.mouse.getX(), love.mouse.getY()) < button.radius then
      score = score + 1

      button.x = math.random(button.radius, love.graphics.getWidth()-button.radius)
      button.y = math.random(button.radius, love.graphics.getHeight()-button.radius)

    end
  end
end

function getDistance(x1, y1, x2, y2)
  temp = (y2-y1)^2+(x2-x1)^2
  return math.sqrt(temp)
end
