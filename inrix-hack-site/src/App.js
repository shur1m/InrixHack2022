import './App.css';
import IconButton from './components/IconButton'

function App() {
  return (
    <>
      <div className='container'>
        <h1 className = 'text-3xl font-bold underline'> The Best Application Ever </h1>
      </div>

      <div>
        <IconButton icon = 'Hello' onClick = {() => {console.log('hi')}}/>
        <button> Two </button>
        <button> Three </button>
      </div>
    </>
  );
}

export default App;
