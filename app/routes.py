from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.services.extractor import extract_file_content
from app.services.model_output import model_output
from models.model import PromptResponse


router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = extract_file_content(file.filename, content)
        return JSONResponse(content={"text": text})
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/prompt_response")
async def prompt_response(data: PromptResponse):
    try:
        prompt = data.prompt
        text = """Rajesh Sagurupilla\nVijayawada, Andhra Pradesh, 520012 |\nsagurupillarajesh220@gmail.com\n| \nhttps://www .linkedin.com/in/rajesh-sagurupilla\nEDUCA TION\nNxtwave Disruptive Technologies \nIndustry Ready Certification in Full-stack Development\nDec ’21 - Ongoing\nVikas Gr oup of Institutions, Vijayawada \nB Tech (Bachelor of Technology)_Computer Science Engineering (CSE) (6.82 CGP A)\n2016 - 2020\nSri Chaitanya Junior  College, Vijayawada \nIntermediate_MPC (69.0%)\n2014 - 2016\nSri Gowtham High School, Vijayawada \nSecondary School Of Certificate (8.0 CGP A)\n2013 - 2014\nSKILLS\nFrontend\n:  HTML, CSS, Bootstrap, JavaScript, React.js* \nBackend\n:  Python, Express, Node.js \nDatabases\n:  SQLite\n*courses yet to be completed\nPROJECTS\nFood Munch (\nfoodmunchrk1415.ccbp.tech\n) \nDeveloped a responsive website for Food Store where users can see a list of food items, detailed information\nabout a food item, of fers \n●\nDesigned page using following HTML  structure elements like li, header , article, footer elements and \ndifferent bootstrap components to show dif ferent sections in the website and dif ferent bootstrap classes \nfor responsiveness through mobile-first approach. \n●\nImplemented product youtube videos by using bootstrap embed and model components \nTechnologies used:\nHTML, CSS, Bootstrap\nTyping Speed Test(\nrkspeedtyping.ccbp.tech\n)\nDeveloped an application which measuring time he took to complete given paragraph \n●\nMaintained timer by using APIs setT imeInterval, clearT imeInterval and Updated timer in the UI \ndynamically using JavaScript DOM operations for every 1 second. \n●\nFetched the paragraph from server asynchronously using fetch GET  HTTP  API call and displayed it on \nUI by using JavaScript DOM Operations. \n●\nDisplayed time that user took in the UI using JavaScript event listeners once user clicked on submit\nbutton, Did form validations for incomplete paragraph. \nTechnologies used:\nHTML, CSS, JS, REST  API Calls,\nBootstrap\nEmoji Game (\nrkemogigame.ccbp.tech\n)\nDeveloped responsive Emoji memory game where users can win it by clicking unique emoji each time till all\ndisplayed emojis are clicked. All emojis positions will be randomized after each click \n●\nList of Emojis is displayed by using React components, props , lists, conditional rendering, styled using\nCSS and randomized emojis placed using event listeners by updating react state. \n●\nUpdated dif ferent game states such as emojis list, winning state and losing state by using game state \nvariable and conditional rendering. \nTechnologies used:\nReact JS, CSS, Bootstrap\n"""
        model_name = data.model_name
        response = model_output(prompt, text, model_name)
        return JSONResponse(content={"Response": response})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
