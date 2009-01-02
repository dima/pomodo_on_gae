package pomodo.models {
  import org.ruboss.collections.ModelsCollection;
  import org.ruboss.models.RubossModel;
  
  [Resource(name="projects")]
  [Bindable]
  public class Project extends RubossModel {
    public static const LABEL:String = "name";

    public var name:String;

    public var notes:String;

    public var startDate:Date;

    public var endDate:Date;

    public var completed:Boolean;

    [BelongsTo]
    public var user:User;

    [HasMany]
    public var tasks:ModelsCollection;
    
    public function Project() {
      super(LABEL);
    }
  }
}
