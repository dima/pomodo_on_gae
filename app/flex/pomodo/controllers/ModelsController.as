package pomodo.controllers {
  import org.ruboss.Ruboss;
  import org.ruboss.collections.RubossCollection;
  import org.ruboss.events.CacheUpdateEvent;
  import org.ruboss.utils.RubossUtils;
  
  import pomodo.models.Project;
  import pomodo.models.ProjectCategory;
  import pomodo.models.Sprint;
  import pomodo.models.Task;
  
  [Bindable]
  public class ModelsController {
    
    public static var controller:ModelsController;
            
    private var _selectedProject:Project;
    
    public var projectCategories:RubossCollection;
        
    public var projectsAndAny:RubossCollection;
    
    public var projects:RubossCollection;
    
    public var incompleteTasks:RubossCollection;
    
    public var tasks:RubossCollection;
        
    public var sprints:RubossCollection;
    
    public function ModelsController(enforcer:SingletonEnforcer) {
      Ruboss.models.addEventListener(CacheUpdateEvent.ID, onCacheUpdate);
      Ruboss.models.indexAll(ProjectCategory, Project, Sprint, Task);
    }

    private function onCacheUpdate(event:CacheUpdateEvent):void {
      if (event.isFor(Project)) {
        projectsAndAny = Ruboss.merge(Ruboss.models.cached(Project), [Project.ANY]);
        projects = Ruboss.models.cached(Project);
      } else if (event.isFor(ProjectCategory)) {
        projectCategories = Ruboss.filter(Ruboss.models.cached(ProjectCategory), filterByCategoryWithNoParent);
      } else if (event.isFor(Task)) {
        tasks = Ruboss.models.cached(Task);
        incompleteTasks = Ruboss.filter(Ruboss.models.cached(Task), filterByCompletionAndProject); 
      } else {
        var prop:String = RubossUtils.toCamelCase(Ruboss.models.state.controllers[event.fqn]);
        if (hasOwnProperty(prop)) {
          this[prop] = Ruboss.models.cache.data[event.fqn];
        }
      }
    }
    
    private function filterByCategoryWithNoParent(item:ProjectCategory):Boolean {
      return item.parent == null;
    }

    public function get selectedProject():Project {
      return _selectedProject;
    }
    
    public function set selectedProject(project:Project):void {
      _selectedProject = (Project.ANY == project) ? null : project;
      filterTasks();
    }

    public function filterTasks(text:String = null):void {
      if (!RubossUtils.isEmpty(text)) {
        incompleteTasks.filterFunction = function(task:Task):Boolean {
          return filterByCompletionAndProject(task) && (task.name.search(new RegExp(text, "i")) != -1);
        };
      } else {
        incompleteTasks.filterFunction = filterByCompletionAndProject;
      }
      incompleteTasks.refresh();
    }

    public function filterByCompletionAndProject(task:Task):Boolean {
      return incompleteTask(task) && taskOfSelectedProject(task);
    }
    
    public function incompleteTask(task:Task):Boolean {
      return !task.completed;
    }
    
    public function taskOfSelectedProject(task:Task):Boolean {
      return (selectedProject) ? task.sprint.project == selectedProject : true;
    }
    
    public static function get instance():ModelsController {
      initialize();
      return controller;
    }
    
    public static function initialize():void {
      if (!controller) controller = new ModelsController(new SingletonEnforcer);
    }
  }
}

class SingletonEnforcer {}